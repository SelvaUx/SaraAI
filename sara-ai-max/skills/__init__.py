"""Skills - Skill-based task execution framework."""

from .base_skill import BaseSkill, SkillResult
from .web_search import WebSearchSkill
from .send_message import SendMessageSkill

__all__ = [
    'BaseSkill',
    'SkillResult',
    'WebSearchSkill',
    'SendMessageSkill',
]
