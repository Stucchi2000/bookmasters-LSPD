#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd

    def search(self, label, keyword, out_label=None):
        mask = self[label].str.contains(keyword, case=False, na=False, regex=False).values
        if out_label is not None:
            out = self[out_label][mask]
        else:
            out = self[label][mask]
        return out, mask
