import torch

# Tensor is one dim = [1,2,3,4,5]

new_tensor = torch.tensor([1,2,3,4,5]) #Example tensor, any shape and any dim

ranger_tens = torch.arange(start=1,end=100,step=5) #Tensor with range from 1 to 100 while stepping 5

MATRIX = torch.tensor([1,7],[7,4]) #Matrix, var name caps locked, dim=2

vector = torch.tensor([1,2]) #Vector = one dim tensor

zeros_tens = torch.zeros(size=(1,5)) #Tensor with filled zeros with size 1,5, zeros_tens.ndim == 2

zeros_like = torch.zeros_like(zeros_tens) = #Creates zero filled tensor which's attributes same with zeros_tens

#example_tensor.ndim = to get the dimention
#example_tensor.size() = to get size of tensor
#Tensor arrtibutes = dtype=None,device=None; dtype == datatype, device == CPU/GPU