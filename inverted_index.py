def inverted_index(doc_list):
    inverted_index_dict = {}
    for d in doc_list:
        id = d['id']
        content = d['content'].split(' ')
        for cont in content:
            if cont in inverted_index_dict.keys():
                if id not in inverted_index_dict[cont]:
                    inverted_index_dict[cont] = inverted_index_dict[cont] + [id]
            else:
                inverted_index_dict[cont] = [id]
    return inverted_index_dict

doc_list = [
  {
    "id": 1,
    "content": "This is the content of document 1 it is very short"
  },
  {
    "id": 2,
    "content": "This is the content of document 2 it is very long bilabial bilabial heheh hahaha ..."
  },
]

print(inverted_index(doc_list))
