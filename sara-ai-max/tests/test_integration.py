"""Test Integration - End-to-end integration tests."""

import pytest
import asyncio
from sara_core.nlu import NLUEngine
from sara_core.planner import Planner
from sara_core.executor import Executor
from sara_core.security import SecurityManager
from sara_core.context import ContextManager


class TestIntegrationPipeline:
    """Test the complete Sara AI Max pipeline."""
    
    @pytest.mark.asyncio
    async def test_time_query_pipeline(self):
        """Test complete pipeline for time query."""
        # Setup
        security = SecurityManager()
        context = ContextManager()
        nlu = NLUEngine()
        planner = Planner(security)
        executor = Executor(security, context)
        
        # Execute pipeline
        intent = nlu.parse("what time is it?")
        plan = planner.create_plan(intent)
        result = await executor.execute(plan)
        
        # Verify
        assert result.success is True
        assert "time" in result.message.lower()
    
    @pytest.mark.asyncio
    async def test_unknown_command_pipeline(self):
        """Test pipeline with unknown command."""
        # Setup
        security = SecurityManager()
        context = ContextManager()
        nlu = NLUEngine()
        planner = Planner(security)
        executor = Executor(security, context)
        
        # Execute pipeline
        intent = nlu.parse("random gibberish command")
        plan = planner.create_plan(intent)
        result = await executor.execute(plan)
        
        # Should gracefully handle unknown commands
        assert result.success is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
