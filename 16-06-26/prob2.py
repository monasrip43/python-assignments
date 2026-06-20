class WordAnalyzer:
    def __init__(self):
        self.words=[]
    def load_words(self):
        try:
            with open("students.txt","r") as file:
                for line in file:
                    word=line.strip()
                    if word:
                        self.words.append(word)
        except FileNotFoundError:
            print("File Not Found")
        
    def get_frequency(self,word):
        return self.words.count(word)
if __name__ == "__main__":
    analyzer=WordAnalyzer()
    analyzer.load_words()
    try:
        query=input()
        if not query.isalpha():
            print("Invalid input")
        else:
            print(analyzer.get_frequency(query))
    except Exception:
        print("Invalid input")
