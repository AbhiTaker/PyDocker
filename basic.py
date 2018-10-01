import docker 

client = docker.from_env()       # Client object to communicate with docker daemon

def clientOperation():
    '''functions associated with client'''

    print('Data Usage Stat:')
    for key,value in client.df().items():
        print('{} : {}'.format(key, value))

    print('System wide Information:')
    for key,value in client.info().items():
        print('{} : {}'.format(key, value))

    '''Other Function : ping(), version(), login(), events(), close()'''


def main():

    while True:

        print(''' OPTIONS: \n
                1. RUN Container \n
                2. LIST Container \n
                3. STOP Container \n
                4. EXIT''')

        option = input('Select Option: ')

        if option == 'RUN Container':
            ImageName = input('Enter Image Name:')
            print(client.containers.run(ImageName, detach=True))

        elif option == 'LIST Container':
            print(client.containers.list())
        
        elif option == 'EXIT':
            break
        
        else:
            print('Inavalid Command')

    



if __name__=="__main__":
    main()
