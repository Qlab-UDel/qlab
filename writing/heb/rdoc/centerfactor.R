centerfactor <- function(x,referencelevels=1:(numlevels-1)) {
	# Centers the Helmert coding of a factor and returns the
	# appropriate contrast coding
	#
	# sample use:
	#   contrasts(Alice$BEFOREKP) = centerfactor(Alice$BEFOREKP)
	#
	# The 2nd parameter, REFERENCELEVELS, controls which level is the
	# reference level for each of the contrasts.  There should be
	# k-1 reference levels, where k is the number of levels of the factor.
	#
	# Reference levels may either be specified with the numerical indices
	# of the factor levels, or the names of the levels.
	#
	# Suppose the three levels of MyData$CUETYPE were 'InvalidCue',
	# 'NoCue', and 'ValidCue' (N.B. R puts factor levels in alphabetical
	# order by default).
	# Then you could do:
	#   contrasts(MyData$CUETYPE) = centerfactor(MyData$CUETYPE,c(2,1))
	# or:
	#   contrasts(MyData$CUETYPE) = centerfactor(MyData$CUETYPE,
	#       c('NoCue','InvalidCue'))
	#
	# Contrast 1 would compare ValidCue and InvalidCue against NoCue,
	# and Contrast 2 would then compare ValidCue against InvalidCue
	#
	# The reference level always get the negative weight.  This decision
	# DOES NOT affect your statistical tests, just the sign
	# of the parameter estimate.
	#
	# DISCLAIMER: I've used this on a number of my datasets and it works
	# properly, but I'm sure I haven't tested it on every possible design.
	# It would be a good idea to check the contrast codes set by the
	# function to make sure they are sensible.
	#
	# 06.19.10 - S.Fraundorf - first version
	# 08.08.10 - S.Fraundorf - excludes NAs.  more efficient
	#                           processing of default value
	# 08.12.10 - S.Fraundorf - bugfixes, supports factor w/ 3 levels!
	# 12.21.10 - S.Fraundorf - supports any # of levels!  can take
	#                           level NAMES as input.  checks to make
	#                           sure the right # of ref. levels specified
	# 01.31.11 - S.Fraundorf - fixed a bug when there were >2 levels and
	#                           each had a different number of observations
	
	# if this is not a factor
	if (is.factor(x) == FALSE) {
		message = paste('converted into a factor from',class(x),sep=' ')
		warning(message)
		x = as.factor(x)
	}
					
	# remove NA values
	x <- na.omit(x)
	
	# get number of levels
	numlevels = length(levels(x))		
	numcontrasts = numlevels - 1
    # get the number of observation at each level
	numobs <- summary(x)
	# get the TOTAL number of observations
	totalobs <- sum(numobs)
	
	# check to make sure the right number of reference levels were specified
	if (length(referencelevels) != numcontrasts) {
		# if not, display error message and stop
		message = paste('Wrong number of reference levels!  There are', 
		  numcontrasts, 'contrast(s) needed, but', length(referencelevels),
		  'reference level(s) specified', sep= ' ')
	    stop(message)
	}
		
	
	# convert the reference levels from characters to numbers, if needed
	if (is.character(referencelevels)) {
		newreflevels = vector(length=numcontrasts)
		for (i in 1:numcontrasts) {
			matches = which(levels(x) == referencelevels[i])
			if (length(matches) == 0) {
				# no matches
				message = paste('Factor does not have a level named', 
				     referencelevels[x], sep = ' ')
		        stop(message)
		    }
		    newreflevels[i] <- matches[1]
		}
		referencelevels <- newreflevels
	}
	
	# set up the contrast matrix
	mymatrix = matrix(nrow=numlevels,ncol=numcontrasts)
					
	# do each contrast
	for (i in 1:numcontrasts) {
		
		# previous reference levels - to be zeroed out
		prevreferencelevels <- referencelevels[1:i-1]
		mymatrix[prevreferencelevels,i] <- 0
		
		# current reference level - always a -.5
		mymatrix[referencelevels[i],i] <- -.5
		
		# positive weighted levels:
		numpos = numlevels-i # number of positive levels
		mymatrix[is.na(mymatrix[,i]),i] <- .5 # was <- posweight
		
		# mean-center
		contrastmean <- (sum(numobs * mymatrix[,i]))/totalobs
		mymatrix[,i] <- mymatrix[,i] - contrastmean
	
	}
	
	return(mymatrix)
	
}
