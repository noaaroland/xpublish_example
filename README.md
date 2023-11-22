# xpublish_example

This is a self-contained small example which shows how to build and publish an aggregated data set from netCDF CF gridded input files.

kerchunk_01.py prepares the files to be served. It's unnesseary for this exmaple (you could open the two files in each of the 3 time series as an aggregation using xarray directly), but illustrates what you would do if the netCDF data files were on cloud storage (S3 buckets).

server.py does the "union" aggregation into one end-point which serves all 3 data variables.

The .nc files are the data inputs.
