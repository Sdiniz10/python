from .api import api_v1_bp
from .dashboard_controllers import dashboard_bp
from .tarefas_controllers import tarefas_bp
from .auth_controllers import auth_bp
__all__ = ["dashboard_bp", "tarefas_bp", "api_v1_bp", "auth_bp"]
