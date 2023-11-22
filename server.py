import xarray as xr
import xpublish
from xpublish import Dependencies, Plugin, SingleDatasetRest, hookimpl

ds_jel = xr.open_dataset("average_jel.json", chunks={'ocean_time': 1})
ds_salt = xr.open_dataset("average_salt.json", chunks={'ocean_time': 1})
ds_temp = xr.open_dataset("average_temp.json", chunks={'ocean_time': 1})

ds = xr.merge([ds_jel, ds_salt, ds_temp])

rest_collection = xpublish.Rest({"B10K-K20_CORECFS_Level1_collection": ds})
rest_collection.serve(port=8970)
