from extract import extract
from transform import transform
from load import load
from analyse import analyse

raw = extract()
clean = transform(raw)
load(clean)
analyse()