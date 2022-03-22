# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import netCDF4 as nc4
from netCDF4 import Dataset
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import calendar

test = nc4.Dataset('C:\\Users\\nkulelekom.SEAHARVEST\\OneDrive - Sea Harvest\\TemporalSafeKeeping\\Linux Temporal\\DataDownolad\\Clean Scripts\\Chloro_Monthly\\2012\\T20120012012031.L3m_MO_CHL_chlor_a_4km.nc')
print(test)
# reading in netCDF file
ifile = 'C:\\Users\\nkulelekom.SEAHARVEST\\OneDrive - Sea Harvest\\TemporalSafeKeeping\\Linux Temporal\\DataDownolad\\Clean Scripts\\Chloro_Monthly\\2012\\T20120012012031.L3m_MO_CHL_chlor_a_4km.nc'

f = Dataset(ifile, mode='r')
lons = f.variables['lon'][:]
lats = f.variables['lat'][:]
field = f.variables['chlor_a'][:,:,:]
f.close()

# create 2D fields of lons and lats
[lons2d, lats2d] = np.meshgrid(lons, lats)

# set up figure and map projection
fig, ax = plt.subplots(3, 4, sharex=True, sharey=True, figsize=(5.5, 3.98),
                       subplot_kw={'projection':ccrs.PlateCarree()})

# flatten axes object
axflat = ax.flat

# define contour levels
levels = np.linspace(0, 800, 9)

# loop through months
for m in np.arange(12):
    
# extract one month data field
    mfield = field[m,:,:]

# contour data
mymap = axflat[m].contourf(lons2d, lats2d, mfield, levels,
                           transform=ccrs.PlateCarree(),
                           cmap=plt.cm.rainbow, extend='max')
# format map
axflat[m].coastlines()
axflat[m].set_extent([-20, 55, -35, 40], crs=ccrs.PlateCarree())

# format gridlines and labels
gl = axflat[m].gridlines(draw_labels=True, linewidth=0.5, color='black',
                         alpha=0.5, linestyle=':')

gl.xlabels_top = False
if (m < 8): gl.xlabels_bottom = False
gl.xlocator = mticker.FixedLocator(np.arange(-180, 180, 20))
gl.xformatter = LONGITUDE_FORMATTER
gl.xlabel_style = {'size':5, 'color':'black'}
gl.ylabels_right = False
if (m not in [0,4,8]): gl.ylabels_left = False
gl.ylocator = mticker.FixedLocator(np.arange(-90, 90, 20))
gl.yformatter = LATITUDE_FORMATTER
gl.ylabel_style = {'size':5, 'color':'black'}

# add label for month
axflat[m].text(-16, -25, calendar.month_abbr[m+1], fontsize=5,
               horizontalalignment='left', verticalalignment='center',
               fontweight='bold')

# make plot look nice
plt.tight_layout(h_pad=0, w_pad=-5, rect=[0,0.1,1,1])

# add colorbar
cbarax = fig.add_axes([0.2, 0.07, 0.6, 0.02])
cbar = plt.colorbar(mymap, cax=cbarax, orientation='horizontal')
cbar.set_label('Precipitation [mm]', rotation=0, fontsize=7, labelpad=1)
cbar.ax.tick_params(labelsize=5, length=0)

# save figure to file
plt.savefig('../images/7_python_multiple_maps_300dpi.png', format='png',
            dpi=300)
# close plot
plt.close()


# this is just to check-- check












