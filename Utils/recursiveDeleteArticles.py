import os
directory = os.getcwd()

def recursiveDeleteArticles(wordLimit):
    for r, _, f in os.walk(r'C:\Users\Catalin\Desktop\bulk-txts-cleaner\Articles'):
        for _f in f:
            apath = os.path.join(r, _f)
            _, ext = os.path.splitext(apath)
            if ext == '.txt':
                try:
                    rflag = False
                    with open(apath) as text:
                        if len(text.read().split()) < wordLimit:
                            rflag = True
                    if rflag:
                        os.remove(apath)
                        print(f'{apath} was deleted')
                except Exception as e:
                    print(f'Error while processing {apath} -> {e}')