class DBRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {
        'weather': {"weather"},
        'detection': {"detection"},
    }

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        for db, apps in self.route_app_labels.items():
            if model._meta.app_label in apps:
                return db
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        for db, apps in self.route_app_labels.items():
            if model._meta.app_label in apps:
                return db
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        for db_, apps in self.route_app_labels.items():
            if app_label in apps:
                return db == db_
        return None
