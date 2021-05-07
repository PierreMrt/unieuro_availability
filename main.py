from scrap_unieuro import Scrapper

LINKS = ['https://www.unieuro.it/online/Notebook/GP66-Leopard-10UG-272IT-pidMSI10UG272IT',
         'https://www.unieuro.it/online/Notebook/FA506QR-HN036T-pidASUFA506QRHN036T',
         'https://www.unieuro.it/online/Notebook/AN515-45-R6Y2-pidACEAN51545R6Y2'
         ]

if __name__ == '__main__':
    for link in LINKS:
        scrapper = Scrapper(link)
        print(scrapper)


