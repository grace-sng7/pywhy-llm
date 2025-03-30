import unittest
from unittest.mock import MagicMock
from guidance.models._openai import OpenAI

from pywhyllm.suggesters.tuebingen_model_suggester import TuebingenModelSuggester, Strategy
from pywhyllm.tests.model_suggester.data_providers.tuebingen_model_suggester_data_provider import *


class TestTuebingenModelSuggester(unittest.TestCase):
    def test_suggest_description(self):
        modeler = TuebingenModelSuggester()
        mock_llm = MagicMock(spec=OpenAI)
        modeler.llm = mock_llm

        mock_llm.__add__ = MagicMock(return_value=mock_llm)
        mock_llm.__getitem__ = MagicMock(return_value=test_suggest_description_expected_response)
        result = modeler.suggest_description(variable)
        assert result == test_suggest_description_expected_result

    def test_suggest_onesided_relationship(self):
        modeler = TuebingenModelSuggester()
        mock_llm = MagicMock(spec=OpenAI)
        modeler.llm = mock_llm

        mock_llm.__add__ = MagicMock(return_value=mock_llm)
        mock_llm.__getitem__ = MagicMock(return_value=test_suggest_onesided_relationship_expected_response)
        result = modeler.suggest_onesided_relationship(variable_a, description_a, variable_b, description_b)
        assert result == test_suggest_onesided_relationship_expected_result

    def test__build_description_program(self):
        modeler = TuebingenModelSuggester()
        mock_llm = MagicMock(spec=OpenAI)
        modeler.llm = mock_llm

        result = modeler._build_description_program(variable)
        assert result == test__build_description_program_expected_result

    def test_suggest_relationship(self):
        modeler = TuebingenModelSuggester()
        mock_llm = MagicMock(spec=OpenAI)
        modeler.llm = mock_llm

        mock_llm.__add__ = MagicMock(return_value=mock_llm)
        mock_llm.__getitem__ = MagicMock(return_value=test_suggest_relationship_expected_response)
        result = modeler.suggest_relationship(variable_a, variable_b, description_a, description_b, domain,
                                              strategy=Strategy.ToT_Single, ask_reference=True)
        assert result == test_suggest_relationship_expected_result

    def test__build_relationship_program(self):
        modeler = TuebingenModelSuggester()
        mock_llm = MagicMock(spec=OpenAI)
        modeler.llm = mock_llm

        result = modeler._build_relationship_program(variable_a, description_a, variable_b, description_b, domain,
                                                     use_description=False, ask_reference=True)
        assert result == test__build_relationship_program_expected_result
