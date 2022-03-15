import deepchem as dc
from deepchem.molnet.load_function.molnet_loader import _MolnetLoader
from typing import Optional

class CustomCsvLoader(_MolnetLoader):
  def create_dataset(self) -> dc.data.Dataset:
    file_name = self.file_name
    loader = dc.data.CSVLoader(self.tasks, feature_field=self.feature_field, featurizer = self.featurizer)
    return loader.create_dataset(file_name)

def load_custom_csv(file_name, 
                    featurizer = None, 
                    splitter = None, 
                    transformers = None, 
                    tasks = ['standard_value'], 
                    feature_field='canonical_smiles',
                    reload: bool = True,
                    data_dir: Optional[str] = None,
                    save_dir: Optional[str] = None,
                    **kwargs):
    loader = CustomCsvLoader(featurizer, splitter, transformers, tasks, data_dir,
                      save_dir, **kwargs) 
    loader.file_name = file_name
    loader.feature_field = feature_field
    return loader.load_dataset(file_name, reload)