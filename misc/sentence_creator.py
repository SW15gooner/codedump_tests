import random
while True:
    sentence=input("Please enter a sentence, with no punctuation except for full stops.\n")
    if sentence!="":
        if sentence[-1]!=".":
            sentence+="."
        SpaceLocation=sentence.find(" ")
        words=sentence.split()
        SentenceStartFile=open("SentenceStartWords.txt","r")
        FileWords=SentenceStartFile.read()
        SentenceStartFile.close()
        FileLines=FileWords.splitlines()
        y=0
        WordFound=False
        z=0
        for x in FileLines:
            SpaceLocation1=x.find(" ")
            word=x[0:SpaceLocation1]
            if word==words[0]:
                WordFound=True
                FileLines[z]+=" "+words[1]
                FileReconstruction=""
                for item in FileLines:
                    FileReconstruction+=item+"\n"
                    SentenceStartFile=open("SentenceStartWords.txt","w")
                    SentenceStartFile.write(FileReconstruction)
                    SentenceStartFile.close()
            z+=1
        if WordFound==False:
            SentenceStartFile=open("SentenceStartWords.txt","w")
            SentenceStartFile.write(FileWords+words[0]+" "+words[1]+"\n")
            SentenceStartFile.close()
        words.pop(0)
        FileLines=FileWords.splitlines()
        w=0
        for a in words:
            SentenceFile=open("SentenceWords.txt","r")
            FileWords=SentenceFile.read()
            SentenceFile.close()
            FileLines=FileWords.splitlines()
            y=0
            WordFound=False
            z=0
            for x in FileLines:
                SpaceLocation1=x.find(" ")
                word=x[0:SpaceLocation1]
                if words[w][-1]==".":
                    if word==words[w]:
                        WordFound=True
                elif word==words[w]:
                    WordFound=True
                    FileLines[z]+=" "+words[w+1]
                    FileReconstruction=""
                    for item in FileLines:
                        FileReconstruction+=item+"\n"
                        SentenceFile=open("SentenceWords.txt","w")
                        SentenceFile.write(FileReconstruction)
                        SentenceFile.close()
                z+=1
            if WordFound==False:
                if words[w][-1]!=".":
                    SentenceFile=open("SentenceWords.txt","w")
                    SentenceFile.write(FileWords+words[w]+" "+words[w+1]+"\n")
                    SentenceFile.close()
            w+=1
    CreatedSentence=""
    SentenceStartFile=open("SentenceStartWords.txt","r")
    FileWords=SentenceStartFile.read()
    SentenceStartFile.close()
    FileLines=FileWords.splitlines()
    TempFileLines=FileWords.splitlines()
    x=0
    while x<len(FileLines):
        WordNum=FileLines[x].count(" ")
        y=0
        for y in range(WordNum):
            TempFileLines.append(FileLines[x])
            y+=1
        x+=1
    x=0
    FileLine=random.choice(TempFileLines)
    FileLineWords=FileLine.split()
    SecondWord=random.choice(FileLineWords[1:])
    CreatedSentence+=FileLineWords[0]+" "+SecondWord
    while CreatedSentence[-1]!=".":
        PreviousWord=CreatedSentence.split()[-1]
        SentenceFile=open("SentenceWords.txt","r")
        FileWords=SentenceFile.read()
        SentenceFile.close()
        FileLines=FileWords.splitlines()
        for x in FileLines:
            FileLineWords=x.split()
            if x.split()[0]==PreviousWord:
                FileLine=x
        FileLineWords=FileLine.split()
        SecondWord=random.choice(FileLineWords[1:])
        CreatedSentence+=" "+SecondWord
    print("\n"+CreatedSentence+"\n")