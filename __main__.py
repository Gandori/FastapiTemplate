import dotenv

import main

if __name__ == '__main__':
    dotenv.load_dotenv()
    server: main.Server = main.Server()
    server.run()
