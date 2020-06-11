import torch
import torch.utils.data as data


BASE_DATA_URL = 'data/'
BASE_DATA_EXTENSION = '.pt'


class CustomDataset(data.Dataset):
    """Custom map-style dataset class"""
    def __init__(self, list_IDs, labels):
        self.list_IDs = list_IDs
        self.labels = labels
    
    def __len__(self):
        """Denotes the total number of samples"""
        return len(self.list_IDs)

    def __getitem__(self, index):
        """Generates one sample of data"""
        sample_ID = self.list_IDs[index]

        X = torch.load(BASE_DATA_URL + sample_ID + BASE_DATA_EXTENSION)
        Y = self.labels[sample_ID]

        return X, Y
