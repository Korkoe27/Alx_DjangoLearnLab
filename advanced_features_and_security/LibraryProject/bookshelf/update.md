---

## **3. update.md**

````markdown
# Update Operation

**Command:**

```python
from bookshelf.models import Book

# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
Book.objects.get(id=book.id).title
```
````