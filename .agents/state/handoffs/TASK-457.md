# Handoff TASK-457

## Status final

done

## Decisões

- password-recovery não aguarda SMTP; e-mail em background
- timeouts no transporter nodemailer

## Causa

- SMTP levou ~24s; front axios timeout 10s
