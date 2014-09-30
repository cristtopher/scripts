for line in $(cat $1); do
    echo "$line";
    ssh-copy-id "$line"
done

#while read line; do echo -e "$line\n"; done < /etc/hosts
