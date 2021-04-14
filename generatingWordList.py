from googletrans import Translator
from datamuse import datamuse

translator = Translator()
api = datamuse.Datamuse()

wlFinalMl = set()
wlFinalTrg = set()
wlTranslatedMl = set()
wlTranslatedTrg = set()

def generatingWordListMl(wordList):

  for word in wordList:
    #print(len(wordList))
    if len(wordList) >= 15:
      break
    
    mlResults = api.words( ml = word, max = 10)

    for result in mlResults:
      res = result.get("word")
      if res not in wordList:
        wlFinalMl.add(res)
        wordList.append(res)

    return wordList
        

def generatingWordListTrg(wordList):

  for word in wordList:
    #print(len(wordList))
    if len(wordList) >= 5:
      break

    mlResults = api.words( rel_trg = word, max = 5)

    for result in mlResults:
      res = result.get("word")
      if res not in wordList:
        wlFinalTrg.add(res)
        wordList.append(res)

  return wordList


def translatingWordList(wordList, type):

  for word in wordList:
    tWord = translator.translate(word, src = 'en', dest = 'pt')
    if type == 1:
      wlTranslatedMl.add(tWord.text)
    else: wlTranslatedTrg.add(tWord.text)

    
def main():

  wordList = ['pandemic','flue','vaccine','quarantine','contagious']

  for word in wordList:

    wlTranslatedMl.add(word)
    wlMl = generatingWordListMl([word])
    # wlTrg = generatingWordListTrg([word])

    translatingWordList(wlMl,1)
    # translatingWordList(wlTrg, 2)
    print("Ml: word= %s, size= %d :" %(word, len(wlMl)), wlMl)
    # print("Trg: word= %s, size= %d :" %(word, len(wlTrg)), wlTrg)


  print("Translateds Final Ml : size= %d :"  %len(wlTranslatedMl), wlTranslatedMl)
  #print("Translateds Final Trg : size= %d :"  %len(wlTranslatedTrg), wlTranslatedTrg)
  #print(wlTranslatedTrg.difference(wlTranslatedMl))


main()