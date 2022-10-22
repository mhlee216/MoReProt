# MoReProt: Molecular Fingerprint Recombination-based Protein Fingerprint.

* PyPI (pip):

```console
$ pip install moreprot
```

* Example (python):

```python
import moreprot

mrp = moreprot.MoReProt(maccs=True, ecfp4=True, ecfp6=True, rdkit=False)
fp = mrp.fingerprint('MATGGRRGAAAAPLLVAVAALLLGAAGHLYPGEVCPGMDIRNNLTRLHELENCSVIEGHL')
```


```python
import pandas as pd
import moreprot
import parmap

def make_fp(inputs):
    mrp, seq = inputs
    return mrp.fingerprint(seq)

df = pd.read_csv('prot.csv')
mrp = moreprot.MoReProt(maccs=True, ecfp4=True, ecfp6=True, rdkit=True)
fps_list = parmap.map(make_fp, [[mrp, seq] for seq in df['sequence'].tolist()], 
                      pm_pbar=True, pm_processes=20)
```
