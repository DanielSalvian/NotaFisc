from services.nf_extractor import NFExtractor

def main():
    nf = NFExtractor()
    print(nf.extract("notafiscaltxt.pdf"))
    
    nfimg = NFExtractor()
    print(nfimg.extract("notafiscalimg.pdf"))


if __name__ == "__main__":
    main()