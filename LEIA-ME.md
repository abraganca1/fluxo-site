# Site Consultoria Fluxo

- `index.html`: site one-page, **versão 3 (22/10/2026)**, espelhando ordem, conteúdo e layout da `2_Apresentacao_Institucional/20261021_Apresentacao_Institucional_Consultoria_Fluxo_v8 [versao Claude].pdf`. Abre direto no navegador.
- `assets/img/`: fotos do ensaio + logos (`logo-azul.png` para fundo branco, `logo-branca.png` para fundo azul).
- `assets/img/clientes/`: logos de clientes (`ppf.png` não é mais usado — cliente saiu da lista vigente; `inhire.png` foi extraído da apresentação v8).
- `assets/img/carreira/`: logos da trajetória do fundador (McKinsey, Newbay, Squadra Sports, Ambev, Esporte Clube Bahia, UFBA), extraídos da apresentação v8.
- Prévia local: `.claude/launch.json` na raiz da área sobe um servidor estático (`npx serve`) na porta 4173 para visualizar com os caminhos relativos funcionando.

## Publicação (GitHub Pages)
- Esta pasta (`3_Site/`) é um repositório git local com remoto em `https://github.com/abraganca1/fluxo-site` (branch `main`), publicado via GitHub Pages com domínio customizado (`CNAME` → www.consultoriafluxo.com.br).
- Autenticação já configurada localmente via Git Credential Manager (token fine-grained da conta `abraganca1`, escopo só deste repositório). Não há token em nenhum arquivo da pasta.
- Identidade dos commits: `Consultoria Fluxo <alvaro@consultoriafluxo.com.br>` (configurada só neste repositório, não afeta outros projetos).
- Para publicar: `git add -A && git commit -m "..." && git push origin main` dentro de `3_Site/`.

## Ordem das seções (igual à apresentação v8)
Capa · Quem somos (com os 4 números) · Clientes · Áreas de atuação (6 cards-resumo) · Abordagem (4 fases) · Formato dos projetos (novo, antes não existia no site) · Fundador (lista de trajetória com logos) · Contato · Apêndice (o que cada prática entrega, com os bullets detalhados — antes era a seção principal "Áreas de atuação").

## Decisões de adaptação (site vs. deck)
- Paleta e tipografia (Source Serif 4 / Albert Sans / Saira) do sistema do site foram **mantidas**, não trocadas pela fonte sans-serif genérica do PDF exportado — é o sistema de marca digital já validado.
- Textos de navegação, botões de CTA e o WhatsApp flutuante são elementos só do site (o deck não tem equivalente).

## Pendências antes de publicar
1. Números do "Quem somos" (+R$100M, +R$50M, +50, +10) já confirmados na apresentação v8 revisada pelo Álvaro.
2. Confirmar autorização dos clientes para exibir os logos (inclui o novo logo da Inhire).
3. Fotos com o ex-sócio (vitor*.jpg, conversa, reuniao, dupla, laptop, parceria) não são mais usadas e podem ir para 99_ARQUIVO.
4. Fonte: títulos em Source Serif 4, textos em Albert Sans, rótulos em Saira (todas gratuitas, Google Fonts). A Prometo da pasta de marca é versão Trial.
5. Hospedagem do domínio consultoriafluxo.com.br (Netlify, Vercel, Hostinger…): basta subir esta pasta.
