---

## **4. delete.md**

````markdown
# Delete Operation

**Command:**

```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
Book.objects.all()
```
````