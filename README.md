
Requirements :
--------------

Python 2.7.x

Check version with the following command:
```bash
python -V
```

Python virtualenv (optional)
```bash
pip install virtualenv
virtualenv --no-site-packages /path/of/your/virtualenv
source /path/of/your/virtualenv/bin/activate
```

Python modules
```bash
pip install -r requirements.txt
```


Launch EpiPlanning :
--------------------

You can run EpiPlanning with default parameters with the following command:
```bash
python EpiPlanning.py
```

Or you can use the class of EpiPlanning.py and give parameters to get_planning method:
```bash
planner EpiPlanning()
planner.get_planning('my_outfile.json', '2015-06-24', '2015-07-24')
```