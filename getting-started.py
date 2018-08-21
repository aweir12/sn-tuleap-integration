
# coding: utf-8

# In[ ]:


import pandas as pd
import requests
import params


# In[ ]:


authURL = params.tuleapURL + 'tokens'


# In[ ]:


r = requests.post(authURL, data = params.tuleapAuthPaylod, headers = params.tuleapHeaders, verify = False)


# In[ ]:


token = r.json()['token']
user_id = r.json()['user_id']


# In[ ]:


params.tuleapHeaders['X-Auth-Token'] = token
params.tuleapHeaders['X-Auth-UserId'] = str(user_id)


# In[ ]:


# Get an artifact to see what it looks like
url = params.tuleapURL + 'trackers/16/artifacts'
r = requests.get(url, headers = params.tuleapHeaders, verify = False)
r.json()


# In[ ]:


# Create A New Artifact
url = params.tuleapURL + 'artifacts'
payload = {"tracker": {"id": 16}, "values": []}

