from function import ekgdata,person
import pandas as pd

ekg_dict = ekgdata.load_by_id(2)
ekgdata1= ekgdata(ekg_dict)
# Plot EKG data with peaks


ekgdata1_peaks= ekgdata1.find_peaks()
print(ekgdata1.find_peaks_index())
print(ekgdata1_peaks)

ekgdata1_hr= ekgdata.estimate_hr(ekgdata1_peaks)
print(ekgdata1_hr)

