#解法一：递归
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next==None:
            return head
        pre=head
        cur=head.next
        pre.next=self.swapPairs(cur.next)
        cur.next=head
        return cur
#解法二：迭代
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next==None: return head
        fakeNode=ListNode(-1)
        fakeNode.next=head      #fakeNode用于定义一个指向head的空节点，可以统一操作
        temp=fakeNode           #fakeNode的指针位置不能
        while temp.next and temp.next.next:
            pre,cur=temp.next,temp.next.next
            temp.next=cur
            pre.next=cur.next
            cur.next=pre
            temp=temp.next.next
        return fakeNode.next