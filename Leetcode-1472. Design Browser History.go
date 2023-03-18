type BrowserHistory struct {
    Url string
    Next *BrowserHistory
    Prev *BrowserHistory
}


func Constructor(homepage string) BrowserHistory {
    Home:=BrowserHistory{
        Url : homepage,
        Next : nil,
        Prev : nil,
    }
    return Home
}


func (this *BrowserHistory) Visit(url string)  {
    NewPage:=BrowserHistory{
        Url : url,
        Next : nil,
        Prev : this,
    }

    this.Next=&NewPage
    this=this.Next
}


func (this *BrowserHistory) Back(steps int) string {
    for steps>0 && this.Prev!=nil{
        this=this.Prev
        steps-=1
    }
    return this.Url
}


func (this *BrowserHistory) Forward(steps int) string {
    for steps>0 && this.Next!=nil{
        this=this.Next
        steps-=1
    }
    return this.Url
}


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */
