# coding: utf-8

def make_tab(string,fig=0):
    for i in range(int(fig)):
        string="\t"+string
    return string

def kaisouka(string):
    string=string.replace(">",">\n")
    string=string.replace(">\n\n",">\n")
    string=string.replace("<","\n<")
    string=string.replace("\n\n<","\n<")
    line=string.split("\n")

    import logger
    import codecs
    f=codecs.open("cgi-bin/tag.conf","r")
#    f=codecs.open("tag.conf","r")
    list_tag=[]
    new_flag="false"
    for tag in f:
         list_tag=tag.split(",")
    f.close()
    #tab:tabキーの数
    tab=0
    for i in line:
        #"<"が含まれていないなら
        if i==i.replace("<",""):
            print make_tab(i,tab)
        #"<"が含まれているなら
        else:
            #"</"が含まれていないなら
            if i==i.replace("</",""):
                print make_tab(i,tab)
                logger.logger(make_tab(i,tab))
                #tag:"</"で閉まらないtagのリスト
                tag_ka=i.split(" ")
                tag=tag_ka[0].lstrip("<").rstrip(">")
                if list_tag.count(tag)!=0:
                    tab+=1
            #"</"が含まれていて、tabが0ではないならば
            else:
                tag=i.lstrip("</").rstrip(">").lstrip("' + '")
                if list_tag.count(tag)==0:
                    list_tag.append(tag)
                    new_flag="true"
                if tab!=0:
                    tab-=1
                print make_tab(i,tab)
    if new_flag=="true":
        new_tag=""
        list_tag=list(set(list_tag))
        for i in list_tag:
            new_tag+=i+","
#        f=open("tag.conf","w")
        f=open("cgi-bin/tag.conf","w")
        f.write(new_tag)
        f.close()

def test_kaisouka(htmldata):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(htmldata)
    print soup.prettify()

if __name__=="__main__":
    kaisouka("<aaa><iii><uuu>aaa</uuu></iii><eee>aa</eee></aaa>")


