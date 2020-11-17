# Install these packages first before you run the script:
# install.packages("devtools")
# devtools::install_github("CrumpLab/jspsychr")
# install.packages("lifecycle") (Please make sure packageVersion("lifecycle") prints ‘0.2.0’)

run_locally <-
  function(path,
           jspsychr_host,
           jspsychr_port,
           show_in,
           participant_id) {
    pr <- plumber::plumber$new()
    
    static_site <- file.path(path, "experiment")
    data_folder <- file.path(path, "data")
    static_router <- plumber::PlumberStatic$new(static_site)
    
    pr$mount("/", static_router)
    
    # Function to save data locally
    pr$handle("POST", "/submit", function(req, res) {
      dat <- jsonlite::fromJSON(req$postBody)
      dat <- readr::read_csv(dat$filedata)
      #tsp <- get_timestamp()
      #file_id <- paste("data", get_timestamp(), get_alphanumeric(10), sep = "_")
      part_id <- participant_id
      dat$part_id <- part_id
      dat <- dat[, c(ncol(dat), 1:ncol(dat) - 1), drop = FALSE]
      readr::write_csv(dat, file.path(data_folder, paste0(part_id, "_lsl", ".csv")))
    })
    
    # add message, and options to display in viewer or browser
    message(
      paste(
        "Point the browser to http://",
        jspsychr_host,
        ":",
        jspsychr_port,
        "?subject=",
        participant_id,
        sep = ""
      )
    )
    
    if (show_in == "viewer") {
      viewer <- getOption("viewer")
      viewer(
        paste(
          "http://",
          jspsychr_host,
          ":",
          jspsychr_port,
          "?subject=",
          participant_id,
          "_lsl",
          sep = ""
        )
      )
    }
    if (show_in == "browser")
      utils::browseURL(
        paste(
          "http://",
          jspsychr_host,
          ":",
          jspsychr_port,
          "?subject=",
          participant_id,
          "_lsl",
          sep = ""
        )
      )
    
    pr$run(swagger = FALSE,
           host = jspsychr_host,
           port = jspsychr_port)
  }



run_locally(
  # Change the path to your local/xslR folder. Please include "". (e.g. "/Users/username/Downloads/local/lslR")
  path = "the path to your local/xslR folder",
  # Host defaults to 127.0.0.1 No need to change, but can be customized (see https://www.rplumber.io/ for more details)
  jspsychr_host = "127.0.0.1",
  # Port defaults to 8000 Don't need to change, but can be customized (see https://www.rplumber.io/ for more details)
  jspsychr_port = 8000,
  # Whehter the experiment should be shown in a browser window or the viewer in R. "browser" for browser, and "viewer" for R viewer.
  show_in = "browser",
  # Enter a customized participant ID. Please include "" . (e.g. "test")
  participant_id = "enter your ID"
)



# This also works. It uses the "jspsychr" library directly, but the name of the data file will not be saved with a customized ID. It will be saved with date and time.
# As the function name (run_locally) is the same as above, you will need to clear your R environment if you run both commands.
# library(jspsychr)
# run_locally(
#   path = "the path to your local/xslR folder",
#   show_in = "browser",
#   jspsychr_host = "127.0.0.1",
#   jspsychr_port = 8000
# )
