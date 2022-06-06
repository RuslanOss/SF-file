1.# U1 = User.objects.create_user(username='Tonny')
2.# U2 = User.objects.create_user(username='Den')
3# Author.objects.create(authorUser=U1)
4# Author.objects.create(authorUser=U2)
5# Category.objects.create(name='Sport')
6# Category.objects.create(name='Movie')
7# Category.objects.create(name='Halth')
8# Category.objects.create(name='Сulture')
9# author = Author.objects.get(id=1)
10# Post.objects.create(author=author, categoryType='NW' , title='sometitle', text='sometext')
11# Post.objects.create(author=author, categoryType='AR' , title='sometitle', text='sometext')
12# Post.objects.create(author=author, categoryType='AR' , title='sometitle', text='sometext')
13# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
14# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))
15# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
16# Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
17# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='somecommenttext')
18# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='somecommenttext')
19# Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='somecommenttext')
20# Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='somecommenttext')
21# Comment.objects.get(id=1).like()
22# Comment.objects.get(id=2).like()
23# Comment.objects.get(id=3).dislike()
24# a = Author.objects.order_by('-ratingAuthor')[:1]
25#  for i in a:
...     #i.ratingAuthor
...     #i.authorUser.username



