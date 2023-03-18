type Trie struct {
    val string
    children map[string]*Trie

}


func Constructor() Trie {
    dict:=Trie{
        val : ".",
        children : make(map[string]*Trie),
    }

    return dict
}


func (this *Trie) Insert(word string)  {
    dict:=this
    for i,ee:=range(word){
        e:=string(ee)
        next,ex:=dict.children[e]
        if ex{
            dict=next
        }else{
            dict.children[e]=&Trie{ val : e, children : make(map[string]*Trie)}
            dict=dict.children[e]
        }

        if i==len(word)-1{
            dict.children["eof"]=&Trie{ val : "eof", children : make(map[string]*Trie)}
        }
    }
}


func (this *Trie) Search(word string) bool {
    dict:=this
    for i,ee:=range(word){
        e:=string(ee)
        next,ex:=dict.children[e]
        if ex{
            dict=next
        }else{
            return false
        }

        if i==len(word)-1{
            _,ex:=dict.children["eof"]
            return ex
        }
    }
    return true
}


func (this *Trie) StartsWith(word string) bool {
    dict:=this
    for _,ee:=range(word){
        e:=string(ee)
        next,ex:=dict.children[e]
        if ex{
            dict=next
        }else{
            return false
        }
    }
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
