import os
import yaml
from src.mlops_wine_prediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """lê o arquivo yaml e retorna seu conteúdo

    Args:
        path_to_yaml (Path): caminho para o arquivo yaml

    Raises:
        ValueError: se o arquivo yaml estiver vazio
        e: exceções gerais

    Returns:
        ConfigBox: tipo ConfigBox
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"arquivo yaml: {path_to_yaml} carregado com sucesso")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("arquivo yaml está vazio")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """cria uma lista de diretórios

    Args:
        path_to_directories (list): lista com caminhos dos diretórios
        verbose (bool, opcional): define se deve logar a criação dos diretórios. Padrão é True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"diretório criado em: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """salva os dados em um arquivo json

    Args:
        path (Path): caminho até o arquivo json
        data (dict): dados a serem salvos no arquivo json
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"arquivo json salvo em: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """carrega os dados do arquivo json

    Args:
        path (Path): caminho até o arquivo json

    Returns:
        ConfigBox: dados acessíveis como atributos de classe (ConfigBox) em vez de dicionário
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"arquivo json carregado com sucesso de: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """salva arquivo binário

    Args:
        data (Any): dados a serem salvos no formato binário
        path (Path): caminho até o arquivo binário
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"arquivo binário salvo em: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """carrega dados do arquivo binário

    Args:
        path (Path): caminho até o arquivo binário

    Returns:
        Any: objeto armazenado no arquivo
    """
    data = joblib.load(path)
    logger.info(f"arquivo binário carregado de: {path}")
    return data
