# An online platform for visual and auditory statistical learning for school-aged children

Contributors: Zhenghan Qi, Yoel Sanchez Araujo, An Nguyen, Anqi Hu, Wendy Georgan, Violet Kozloff, Parker Robbins, and other members of the Language Acquisition and Brain Lab (QLAB) at the University of Delaware

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">An online platform for visual and auditory statistical learning for school-aged children</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Language Acquisition and Brain Laboratory at the University of Delaware</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"> Creative Commons Attribution-NonCommercial 4.0 International License. </a>


All materials are licensed under CC-BY-NC. Materials are free for non-commerical reproductions and modifications as long as users credit and cite the original source. Please see the citation on Zenodo for detailed information. 

Our research is funded by the National Institute on Deafness and Other Communication Disorders (NIDCD).

## Introduction
In this Zenodo project, two versions of the online visual and auditory statistical learning tasks are offered.

- **Local**
- **Remote**

If you are intersted in running the study locally and save all data on your computer, then please refer to the **Local** section below. However, if you are interested in running the study through websites online and save all data on a remote server, please refer to the **Remote** section below.

## Local


#### The local version of the SL tasks will allow you to:

1. Use a R script to run the SL tasks on your computer. This is realized by setting up your computer as a local server. The SL tasks are still presented through a browser window (**Google Chrome is the recommended browser**), but the materials of the study (e.g. stimuli, task scripts) are stored locally.

2. Save the data of the SL tasks on your computer.



#### The local version of the SL tasks will require you to:

1. Run a R script and download a R package called `jspsychr` (https://github.com/CrumpLab/jspsychr). `jspsychr`, provided by Matt Crump, is a R package for "writing and running `jspsych` experiments using R studio". `jspsych` is a javascript library for web-based behavioral experiments written by Josh De Leeuw (https://www.jspsych.org/). As our tasks are originally designed to be run remotely, we developed the task scripts using `jspsych`. Thus, a package like `jspsychr` allows us to completely replicate the use of `jspsych` and the remote SL tasks in a local environment.

2. Download folders that contain the SL task stimuli, SL task scripts, and a R script for running the SL tasks.



#### How does the local version of the SL tasks work?

First, please download the `local` folder. This folder should contain four sub-folders:

- sslR (for the syllable SL task)
- tslR (for the tone SL task)
- lslR (for the letter SL task)
- vslR (for the image SL task)

In each `local/xslR` folder, you should find these sub-folders or files:

- data (where the data of the SL tasks should be saved)
- experiment (where the task scripts and stimuli are)
- run.R (the R script to run the SL task)

In each `local/xslR/experiment` folder, you should find these main things:

- `index.html` (the main script of the SL task)
- `jspsych` library package
- `jspsychr` script in the `jspsychr` folder
- task-specific image or sound stimuli
- `continue.html` (the end page of each experiment)

To run the study, please open `run.R`. This script is adpated from the `jspsychr` package provided by  Matt Crump (https://github.com/CrumpLab/jspsychr/blob/master/R/run_locally.R). 

To run the script, please first install the `jspsychr` package (https://github.com/CrumpLab/jspsychr) using the following commands in R. When you are installing `CrumpLab/jspsychr`, you might be asked to update some packages. 

(Note: During our tests in multiple versions of R and RStudio, we have found that the `run.R` script still worked even if we skipped all the updates. However, if you run into errors running the `run.R` script, we recommend checking the `jspsychr` github page (https://github.com/CrumpLab/jspsychr) to troubleshoot.)

```{r}
install.packages("devtools")
devtools::install_github("CrumpLab/jspsychr")
```
During our tests of the `run.R` script, we found that the package `lifecycle` is also needed. The version of this package must be 0.2.0. Please use the commands below to check the version of the package or update/ install the new version (0.2.0) of `lifecycle`:

```{r}
packageVersion("lifecycle") 
install.packages("lifecycle")
```

Then please run the following command. This is a customized function adpated from  (https://github.com/CrumpLab/jspsychr/blob/master/R/run_locally.R). `participant_id` is added into this customized script so that a customized ID can be assigned to each participant's data.

```{r}
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
      readr::write_csv(dat, file.path(data_folder, paste0(part_id, "_ssl", ".csv")))
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
          "_ssl",
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
          "_ssl",
          sep = ""
        )
      )
    
    pr$run(swagger = FALSE,
           host = jspsychr_host,
           port = jspsychr_port)
  }
```

To start running the experiment, please run the following command. You need to change the  path to your `local/xslR` folder and enter a customized participant ID. The data file will be named as "participantID_xsl.csv" and will be saved in the `local/xslR/data` folder. 


```{r}
run_locally(
  # Change the path to your local/xslR folder. Please include "". (e.g. "/Users/username/Downloads/local/sslR")
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
```

After you run the the command, you should see a browser window pop up. The link of the website should be `http://127.0.0.1:8000/?subject=your_customized_id`. **Now, the experiment is ready!** The browser recommended is **Google Chrome**. For best user experience, we highly recommend you use **Google Chrome** (https://www.google.com/chrome/). If other browsers are used, the stimuli may not be displayed correctly. You can copy the link (`http://127.0.0.1:8000/?subject=your_customized_id`) to a Google Chrome browser if the command below opens other default browsers.

Now, please use the browser and get to the end of the experiment. Data will be saved as "participantID_xsl.csv" in the `local/xslR/data` folder. The participantID will be the customized ID specified in the command above.

After the experiment is finished, you can close the browser window. **And then** you can stop the above command in R by manually pressing the `stop` button in your R console. After the command is terminated, the local server will be down, and the website (`http://127.0.0.1:8000/?subject=your_customized_id`) will also show **This site can’t be reached**. To run the SL task again, you can repeat the steps above.

You may see some warnings in your R console after the command is terminated. For example, there might be a warning about `plumber`. The deprecated version of `plumber` is used as this is used in the `jspsychr` package:

```{r}
Warning message:
`plumber` is deprecated as of plumber 1.0.0.
Please use `Plumber` instead. 
```

At the end of the `run.R` script, you should also find the command below. This command also works. It uses the `jspsychr` library directly, though it generates a slightly different link (`http://127.0.0.1:8000/`). If you use this command instead, the data file will not be saved with a customized ID. It will be saved with date and time.

```{r}
# This also works. It uses the "jspsychr" library directly, but the name of the data file will not be saved with a customized ID. It will be saved with date and time.
# As the function name (run_locally) is the same as above, you will need to clear your R environment if you run both commands.
library(jspsychr)
run_locally(
  path = "the path to your local/xslR folder",
  show_in = "browser",
  jspsychr_host = "127.0.0.1",
  jspsychr_port = 8000
)
```


## Remote

Please check back on this site later. We are working on this section now.














