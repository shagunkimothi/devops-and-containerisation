# ── Stage 1: Builder ──────────────────────────────────────────────────────────
FROM postgres:16-alpine AS builder

COPY init.sql /docker-entrypoint-initdb.d/init.sql

# ── Stage 2: Runtime ──────────────────────────────────────────────────────────
FROM postgres:16-alpine AS runtime

COPY --from=builder /docker-entrypoint-initdb.d/init.sql \
                    /docker-entrypoint-initdb.d/init.sql

USER postgres

EXPOSE 5432
