## Permissions and Group Setup for Bookshelf App

### Custom Permissions on Book Model:
- can_view: View list or detail of books
- can_create: Add new books
- can_edit: Edit existing books
- can_delete: Delete books

### Groups and Assigned Permissions:
- Viewers:
  - can_view

- Editors:
  - can_view
  - can_create
  - can_edit

- Admins:
  - can_view
  - can_create
  - can_edit
  - can_delete

### Enforced in Views:
- Decorators like @permission_required('bookshelf.can_edit') used
