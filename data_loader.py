import os

from PIL import Image
from torch.utils.data import DataLoader
import torchvision
from torchvision.datasets import CIFAR10
import torchvision.transforms as transforms

# reference: https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

BASE_DATA_URL = './data/'
CIFAR10_DATA_URL = './data/cifar10/'
CIFAR10_CLASSES = ('plane', 'car', 'bird', 'cat', 'deer', 
                    'dog', 'frog', 'horse', 'ship', 'truck')

# CIFAR-10 dataloader
def fetch_cifar10_dataloader(batch_size=4, number_of_workers=1):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    
    train_dataset = CIFAR10(root=CIFAR10_DATA_URL, train=True,
                            download=True, transform=transform)
    test_dataset = CIFAR10(root=CIFAR10_DATA_URL, train=False,
                            download=True, transform=transform)

    train_dataloader = DataLoader(train_dataset, batch_size=batch_size,
                                    shuffle=True, num_workers=number_of_workers)
    test_dataloader = DataLoader(test_dataset, batch_size=4,
                                    shuffle=False, num_workers=number_of_workers)

    return train_dataloader, test_dataloader


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    # functions to show an image
    def imshow(img):
        img = img / 2 + 0.5     # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()

    train_dataloader, _ = fetch_cifar10_dataloader()
    # get some random training images
    dataiter = iter(train_dataloader)
    images, labels = dataiter.next()

    # show images
    imshow(torchvision.utils.make_grid(images))
    # print labels
    print(' '.join('%5s' % CIFAR10_CLASSES[labels[j]] for j in range(4)))
