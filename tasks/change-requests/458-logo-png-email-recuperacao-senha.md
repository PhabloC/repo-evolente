# Task 458 - Logo PNG no e-mail de recuperação (compatível com clientes)

## Status

done

## Tipo

back

## Stacks envolvidos

- backend

## Objetivo

Substituir a logo WebP do e-mail por PNG publico no S3, porque clientes de e-mail quebram WebP.

## Resultado da execucao

- Logo ja estava no bucket em WebP (HTTP 200), mas clientes de email nao renderizam WebP
- PNG publicado em `branding/logo-completa.png`
- Default `MAIL_BRAND_LOGO_KEY` atualizado para PNG

## Status final

done
