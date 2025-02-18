class BasicImplementations: 


    def mergeAlternatively(self, word1, word2):
        """
        Takes two words and alternatively appends
        word1: str
        word2: str
        output: str
        """

        try: 

            assert type(word1) == str
            assert type(word2) == str 

            append_list = [j+k for j in word1 for k in word2]
            new_word = ""
            index = None
            for i in range(len(word1)): 
                if word1[i] is not None and word2[i] is not None: 
                    new_word = new_word + word1[i] + word2[i]
                    index = i
                else: 
                    new_word = new_word + word1[i]
                    index = i
            
            if len(word2) > len(word1): 
                new_word = new_word + word2[index+1:]
                

            print(new_word)
            return new_word
        

        except Exception as ex: 
            print(f"Something went wrong {ex}")
    


def main():
    
    #
    b = BasicImplementations()
    word1 = "abc"
    word2 = "pqrs"
    b.mergeAlternatively(word1, word2)

if __name__ == "__main__": main()
