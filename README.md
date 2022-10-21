# MoReProt: Molecular Fingerprint Recombination-based Protein Fingerprint.

* PyPI (pip):

```console
$ pip install moreprot
```


```python
from moreprot import MoReProt

mrp = MoReProt.Fingerprint(maccs=True, ecfp4=True, ecfp6=True, rdkit=True)
fp = mrp.proteinfp('MATGGRRGAAAAPLLVAVAALLLGAAGHLYPGEVCPGMDIRNNLTRLHELENCSVIEGHL')
```
