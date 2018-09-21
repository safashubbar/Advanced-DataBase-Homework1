
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'google.cloud.bigquery')


# In[6]:


get_ipython().run_cell_magic('bigquery', 'top_five_states ', 'SELECT\n    state AS state,\n    COUNT(1) AS birth_count\nFROM `bigquery-public-data.samples.natality`\nGROUP BY state\nORDER BY birth_count DESC\nLIMIT 6')


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


top_five_states.plot(kind='bar', x='state', y='birth_count');


# In[15]:


top_five_states.plot(x='state');


# In[9]:


get_ipython().run_cell_magic('bigquery', 'top_five_states_with_Ohio', "SELECT\n    state AS state, birth_count from (SELECT state,\n    COUNT(1) AS birth_count\nFROM `bigquery-public-data.samples.natality`\nGROUP BY state\nORDER BY birth_count DESC\nLIMIT 7)\n    \nUNION ALL\n\nSELECT\n    state,\n    COUNT(1) AS birth_count\nFROM `bigquery-public-data.samples.natality`\nWHERE state='OH'\nGROUP BY state\nORDER BY birth_count DESC\nLIMIT 7")


# In[10]:


top_five_states_with_Ohio.plot(kind='bar', x='state', y='birth_count');


# In[11]:


from google.cloud import bigquery
client = bigquery.Client()
sql = """
SELECT
    mother_age,
    COUNT(1) AS count,
    year
FROM
    `bigquery-public-data.samples.natality`
WHERE
    year>1997 AND year < 2009
GROUP BY
    mother_age, year
ORDER BY
    count DESC
"""
df = client.query(sql).to_dataframe()
df.head()


# In[12]:


pivot_table = df.pivot(index='year', columns='mother_age', values='count')
pivot_table.plot(kind='bar', stacked=True, figsize=(13, 7));


# In[13]:


get_ipython().run_cell_magic('bigquery', 'father_age', 'SELECT\n    year,\n    AVG(father_age) AS AVG_father_age\n\nFROM\n    `bigquery-public-data.samples.natality`\nWHERE\n    year>1997 AND year < 2009\nGROUP BY  year\nORDER BY\n    year DESC\nLIMIT 11')


# In[16]:


father_age.plot(kind='bar', x='year', y='AVG_father_age');


# In[17]:


father_age.plot (x='year', y='AVG_father_age');

