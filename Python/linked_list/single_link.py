# coding:utf-8

# 节点类
class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LianBiao(object):
    def __init__(self):
        self.root = None

    # 给单链表添加元素节点
    def addNode(self, data):
        if self.root:
            # 有头结点，则需要遍历到尾部节点，进行链表增加操作
            cursor = self.root
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = Node(data, None)
        else:
            self.root = Node(data, None)

    # 在链表的尾部添加新节点，底层调用addNode方法即可
    def append(self, value):
        self.addNode(value)

    # 在链表首部添加节点
    def prepend(self, value):
        if self.root:
            cursor = self.root
            self.root = Node(value, cursor)
        else:
            self.root = Node(value, None)

    # 在链表的指定位置添加节点
    def insert(self, index, value):
        if self.root:
            if index <= 0 or index > self.size()+1:
                print('index %d 非法， 应该审视一下您的插入节点在整个链表的位置！')
                return
            # 如果index==1， 则在链表首部添加即可
            if index == 1:
                self.prepend(value)
            elif index == self.size() + 1:
                self.append(value)
            else:
                count = 1
                cursor = self.root
                while count < index-1:
                    count += 1
                    cursor = cursor.next
                tmp = cursor.next
                cursor.next = Node(value, tmp)
        else:
            return

    # 删除指定位置上的节点
    def delNode(self, index):
        if self.root:
            if index <= 0 or index > self.size():
                print('index %d 非法， 应该审视一下您的插入节点在整个链表的位置！')
                return
            if index == 1:
                self.root = self.root.next
            else:
                count = 1
                cursor = self.root
                while count < index-1:
                    count += 1
                    cursor = cursor.next
                cursor.next = cursor.next.next
        else:
            return

    # 删除值为value的链表节点元素
    def delValue(self, value):
        if self.root:
            cursor = self.root
            if cursor.data == value:
                self.root = self.root.next
            while cursor and cursor.next:
                if cursor.next.data == value:
                    cursor.next = cursor.next.next
                cursor = cursor.next
        else:
            return

    # 判断链表是否为空
    def isempty(self):
        if not self.root or self.size() == 0:
            return True
        else:
            return False

    # 删除链表及其内部所有元素
    def truncate(self):
        self.root = None

    # 获取指定位置的节点的值
    def getvalue(self, index):
        if self.root:
            if not self.root or index <=0 or index > self.size():
                print("index %d不合法！"%index)
                return None
            count = 1
            cursor = self.root
            while count < index:
                count += 1
                cursor = cursor.next
            return cursor.data
        else:
            return

    # 获取链表尾部的值，且不删除该尾部节点
    def peek(self):
        return self.getvalue(self.size())

    # 获取链表尾部节点的值，并删除该尾部节点
    def pop(self):
        value = self.peek()
        self.delNode(self.size())
        return value

    # 单链表逆序实现
    # https://blog.csdn.net/wxn704414736/article/details/79831833
    # 思路：建立一个空head,用1临时变量tmp记录当前位置(如果直接指向head，后面的数据就会丢失)，然后把当前位置指向head
    # head的位置更新为当前位置，当前位置更新为临时变量位置即可，如此循环
    # 最后把逆序后的头节点赋值给root
    def reverse(self):
        if self.root:
            pre = None
            cursor = self.root
            while cursor:
                tmp = cursor.next
                cursor.next = pre
                pre = cursor
                cursor = tmp
            self.root = pre
        else:
            return


    # 修改指定位置节点的值
    def updateNode(self, index, value):
        if self.root == None:
            return
        if index < 0 or index > self.size():
            return
        count = 1
        cursor = self.root
        while count < index:
            count += 1
            cursor = cursor.next
        cursor.data = value

    # 删除链表中的重复元素
    # 记录当前结点和当前节点的上一个结点，并用一个set存放已经包含的元素，
    # 对当前结点，如果当前节点在已有元素的集合中，则说明当前结点重复，
    # 则让当前节点的上一个节点直接指向当前节点的下一个节点；
    # 否则，将当前结点加入到已有元素的集合中
    def delDuplecate(self):
        if self.root == None:
            return
        # 使用一个list来存放即可
        cursor = self.root
        pre = None
        hash_list = []
        while cursor:
            if cursor.data in hash_list:
                pre.next = cursor.next
            else:
                hash_list.append(cursor.data)
                pre = cursor
            cursor = cursor.next

    # 打印链表自身元素
    def Print(self):
        if self.root:
            cursor = self.root
            while cursor:
                print cursor.data
                cursor = cursor.next
        else:
            return

    def size(self):
        count = 0
        if self.root:
            cursor = self.root
            while cursor.next:
                count += 1
                cursor = cursor.next
            count += 1
            return count
        else:
            return count
a = LianBiao()
# a.addNode(1)
# a.prepend(2)
# a.addNode(3)
# a.addNode(2)
# a.insert(3,5)
a.append(1)
a.append(1)
a.append(2)
a.append(3)
a.append(3)
a.append(1)
print a.root.data
print a.root.next.data
print a.root.next.next.data
print a.root.next.next.next.data
print a.root.next.next.next.next.data
print "---------"
a.delDuplecate()
print a.Print()
# a.truncate()
#print a.root.data
#print a.root.next.data
#print a.root.next.next.data
# print a.root.next.next.next.data
# print a.root.next.next.next.next.data
# print "-----------"
# a.updateNode(5,9)
# print a.root.data
# print a.root.next.data
# print a.root.next.next.data
# print a.root.next.next.next.data
# print a.root.next.next.next.next.data
