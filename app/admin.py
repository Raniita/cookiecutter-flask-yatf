from flask_login import current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

# Override Model View to add role permissions
class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

# Overrida Index View to only allow admin access
class CustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))