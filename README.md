# Trello back-end 구축


## DB 모델링

### User
- username (사용자 구분 필드)
- email
- password
- created_date
- updated_date
<br>

### Board
- title
- bgColor
- user (ManyToManyField)
- created_date
- updated_date
<br>

### List
- title
- boardId (ForeignKey)
- pos
- created_date
- updated_date
<br>

### Card
- title
- description
- pos
- listId (ForeignKey)
- created_date
- updated_date
<br>


(향후 추가 구현)

### Card
- user (ManyToManyField)
- is_done
- labels
<br>

### Activity
- history
- user (ForeignKey)
- card (ForeignKey)
- created_date
- updated_date
<br>

### CheckList
- title
- is_done
- card (ForeignKey)
<br>

