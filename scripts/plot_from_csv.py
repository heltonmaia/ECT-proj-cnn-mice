import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__': 
    data = pd.read_csv('../plots/first_full_train.csv')
    
    epochs = data['epochs'].values
    loss = data['loss'].values


    e = range(0, 10000)

    l1 = loss[:10000]
    l2 = loss[10000:20000]
    l3 = loss[20000::]
    
    plt.title('Loss')
    
    plt.plot(e, l1, 'r-', label='Aron + Nature')
    plt.plot(e, l2, 'g--', label='Aron + Nature + Crim Superior')
    plt.plot(e, l3, 'b-.', label='Aron + Nature + Crim Superior + Crim Side')
    
    plt.legend(loc='upper right')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')

    plt.tight_layout()
    plt.show()
    