#!/bin/env bash
# Adiciona novo bundle no projeto para ser avaliado
if [ "$#" -eq 0 ]; then
  echo -e "Modo de uso:\n\t$0 <bundles/canditato.bundle>"
  exit 1
fi

BUNDLE="$1"
RNAME="$(basename "$BUNDLE")"
BRANCH="bundle/${RNAME%.bundle}"

if [ ! -r "$BUNDLE" ]; then
    echo "Arquivo bundle inválido!"
    exit 1
fi


if [ -n "`git status --porcelain`" ]; then
    echo "Projeto possúi alterações não confirmadas."
    echo "Não é possível continuar"
    exit 1
fi

git remote add $RNAME $BUNDLE
if [ $? != 0 ]; then
    echo "Saindo."
    exit 2
fi

git fetch $RNAME
git checkout -b "$BRANCH" "$RNAME/master"
git push -u results "$BRANCH"
