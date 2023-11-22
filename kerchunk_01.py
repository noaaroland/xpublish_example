import fsspec
from kerchunk.netCDF3 import NetCDF3ToZarr
from kerchunk.combine import MultiZarrToZarr
from pathlib import Path
import os
import ujson
import json
import zarr
import xarray as xr

da_vars = ['jel', 'temp', 'salt']

for var in da_vars:
    fs = fsspec.filesystem('file')
    flist = fs.glob(f'{var}_*.nc')
    fs2 = fsspec.filesystem('file')

    for u in flist:
        ncchunks = NetCDF3ToZarr(u)
        fstem = Path(u).stem
        outf = f'{fstem}.json'
        with fs2.open(outf, 'wb') as f:
            print(outf)
            f.write(ujson.dumps(ncchunks.translate()).encode())

    jfiles = fs.glob('*.json')

    mzz = MultiZarrToZarr(jfiles, concat_dims = ['ocean_time'],  identical_dims = ['lat_rho', 'lon_rho', 's_rho', 'hc', 'Cs_r'])
    filename = f'average_{var}.json'
    d = mzz.translate()
    with fs2.open(filename, 'wb') as f:
        f.write(ujson.dumps(d).encode())

