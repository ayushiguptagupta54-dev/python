def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False
   
papers = ["ayush", "shivam", "kaaju", "siya"]


search_name = "siya"
result = find_paper(papers, search_name)
    
if result:
        print("found")
else:
        print("not found")

