import torch
import proximalGradient as pg

class OneLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        """
        The constructor creates one linear layer and assigns it a name.
        """
        super(OneLayerNet, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, D_out)
        self.linear1.name = "linear1"

    def forward(self, x):
        """
        Simple forward step
        """
        y_pred = self.linear1(x)
        print("linear1:", self.linear1)
        for param in self.linear1.parameters():
            print("param:", param)
            print("param.grad:", param.grad)
        #print("linear1.grad:", self.linear1.grad)
        #print("linear1.grad:", self.linear1.data)
        return y_pred

# Values for the network size
N, D_in, H, D_out = 4, 3, 4, 2
#N, D_in, H, D_out = 4, 3, 10, 5

# Create random Tensors to hold inputs and outputs
x = torch.zeros(N, D_in)
y = torch.ones(N, D_out)
print("x.requires_grad")
print(x.requires_grad)

# Construct our model by instantiating the class defined above
model = OneLayerNet(D_in, H, D_out)
print("model:", model)

criterion = torch.nn.MSELoss(size_average=False)
#optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)
#for t in range(500):
#for t in range(1000):
for t in range(10):
    # Forward pass: Compute predicted y by passing x to the model
    #y_pred, h_relu = model(x)
    y_pred = model(x)



    # Compute and print loss
    #loss = criterion(y_pred, y) + reg_loss
    #loss = criterion(y_pred, y) + torch.sum(model.linear1.weight[:,:])
    cross_entropy_loss = criterion(y_pred, y)
    #loss = cross_entropy_loss + torch.abs(model.linear1).sum()
    #loss = cross_entropy_loss + torch.abs(h_relu).sum() * reg_lambda
    #loss = cross_entropy_loss + torch.abs(model.linear1.weight).sum() * reg_lambda
    loss = cross_entropy_loss# + torch.abs(model.linear1.weight).sum() * reg_lambda
#    print("y_pred\t\t\t\t\t\t", y_pred.transpose(0,1))
#    print("y\t\t\t\t\t\t", y.transpose(0,1))
#    print("y_pred.grad: ")
#    print(y_pred.grad)
#    print(y_pred.grad_fn)
#    print("x.grad")
#    print(x.grad)
#    print("loss:", loss)
#    print("loss.grad_fn", loss.grad_fn)
#    print(loss.grad_fn.next_functions[0][0])
#    print(loss.grad_fn.next_functions[0][0].next_functions[0][0])
#    print(loss.grad_fn.next_functions[0][0].next_functions[0][0].next_functions[0][0])
    #print(model.linear1.grad)
    #print(t, loss.item())
    #print(h_relu)


    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
#    print("model.linear1.weight.grad:", model.linear1.weight.grad)
#    print("model.linear1.bias.grad:", model.linear1.bias.grad)
#    print("model.linear1.weight before:", model.linear1.weight)
#    print("model.linear1.bias before:", model.linear1.bias)
    optimizer.step()
#    print("model.linear1.weight after:", model.linear1.weight)
#    print("model.linear1.bias after:", model.linear1.bias)
#    print("model.linear1.weight.norm():", model.linear1.weight.norm())

    print("weight before:", model.linear1.weight)
    print("bias before:", model.linear1.bias)
    #pg.l21(model.linear1)
    #pg.l21(model.linear1, reg=0.1, lr=optimizer.lr)
    #pg.l21(model.linear1, reg=0.01)
    #pg.l21(model.linear1, reg=0.1)
    #pg.l21_slow(model.linear1.weight, reg=0.1)
    #pg.l21(model.linear1.weight, reg=0.1)
    #pg.l21(model.linear1.weight, model.linear1.bias, reg=0.1) #TODO: Make test, test both of these
    #print("weight after:", model.linear1.weight)
    #print("bias after:", model.linear1.bias)

    # Seeing about l2...
    #print("L2:", model.linear1.weight.norm(2))
    #print("weight before:", model.linear1.weight)
    #pg.l2(model.linear1.weight, model.linear1.bias, reg=0.1)
    #print("weight after:", model.linear1.weight)


    #L1...
    #print("weight before:", model.linear1.weight)
    #pg.l1(model.linear1.weight, model.linear1.bias, reg=0.1)
    #print("weight after:", model.linear1.weight)


    #Linf1...
    print("weight before:", model.linear1.weight)
    print("bias before:", model.linear1.bias)
    pg.linf1(model.linear1.weight, model.linear1.bias, reg=0.1)
    print("weight after:", model.linear1.weight)
    print("bias after:", model.linear1.bias)

    #Linf
    #print("weight before:", model.linear1.weight)
    #pg.linf(model.linear1.weight, model.linear1.bias, reg=0.1)
    #print("weight after:", model.linear1.weight)
    
    #Elastic Net
    #print("weight before:", model.linear1.weight)
    #pg.elasticnet(model.linear1.weight, model.linear1.bias, reg=0.1)
    #print("weight after:", model.linear1.weight)
 
    #Log Barrier...
    #print("weight before:", model.linear1.weight)
    #pg.logbarrier(model.linear1.weight, model.linear1.bias, reg=0.1)
    #print("weight after:", model.linear1.weight)

